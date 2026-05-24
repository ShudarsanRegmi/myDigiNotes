```python
from neo4j import GraphDatabase
import logging
from pprint import pprint

# =========================================================
# LOGGING CONFIGURATION
# =========================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logger = logging.getLogger(__name__)

# =========================================================
# DATABASE CONFIG
# =========================================================

URI = "bolt://localhost:7687"
USERNAME = "neo4j"
PASSWORD = "12345678"

# =========================================================
# DRIVER SETUP
# =========================================================

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

# =========================================================
# HELPER
# =========================================================

def print_header(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# =========================================================
# RESET DATABASE
# =========================================================

def reset_database(tx):
    logger.info("Deleting existing graph...")
    tx.run("MATCH (n) DETACH DELETE n")


# =========================================================
# CREATE SAMPLE GRAPH
# =========================================================

def create_graph(tx):

    logger.info("Creating sample graph...")

    query = """
    CREATE
    (alice:Person {
        name: 'Alice',
        age: 22
    }),

    (bob:Person {
        name: 'Bob',
        age: 25
    }),

    (charlie:Person {
        name: 'Charlie',
        age: 28
    }),

    (david:Person {
        name: 'David',
        age: 30
    }),

    (openai:Company {
        name: 'OpenAI'
    }),

    (google:Company {
        name: 'Google'
    }),

    (python:Skill {
        name: 'Python'
    }),

    (cyber:Skill {
        name: 'Cybersecurity'
    }),

    (ml:Skill {
        name: 'Machine Learning'
    }),

    (proj1:Project {
        name: 'Threat Detector'
    }),

    (proj2:Project {
        name: 'AI Chatbot'
    })

    CREATE
    (alice)-[:KNOWS]->(bob),
    (bob)-[:KNOWS]->(charlie),
    (charlie)-[:KNOWS]->(david),

    (alice)-[:WORKS_AT]->(openai),
    (bob)-[:WORKS_AT]->(google),

    (alice)-[:HAS_SKILL]->(python),
    (alice)-[:HAS_SKILL]->(cyber),

    (bob)-[:HAS_SKILL]->(python),
    (bob)-[:HAS_SKILL]->(ml),

    (charlie)-[:HAS_SKILL]->(cyber),

    (alice)-[:BUILT]->(proj1),
    (bob)-[:COLLABORATED_ON]->(proj1),

    (bob)-[:BUILT]->(proj2),
    (charlie)-[:COLLABORATED_ON]->(proj2)
    """

    tx.run(query)


# =========================================================
# BASIC NODE QUERY
# =========================================================

def get_all_people(tx):

    print_header("ALL PEOPLE")

    query = """
    MATCH (p:Person)
    RETURN p.name AS name, p.age AS age
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# FILTERING
# =========================================================

def people_above_age(tx, age):

    print_header(f"PEOPLE ABOVE AGE {age}")

    query = """
    MATCH (p:Person)
    WHERE p.age > $age
    RETURN p.name AS name, p.age AS age
    """

    result = tx.run(query, age=age)

    for record in result:
        pprint(dict(record))


# =========================================================
# RELATIONSHIP QUERY
# =========================================================

def get_skills(tx, person_name):

    print_header(f"SKILLS OF {person_name}")

    query = """
    MATCH (p:Person {name:$name})-[:HAS_SKILL]->(s:Skill)
    RETURN s.name AS skill
    """

    result = tx.run(query, name=person_name)

    for record in result:
        pprint(dict(record))


# =========================================================
# MULTI-HOP TRAVERSAL
# =========================================================

def friends_of_friends(tx):

    print_header("FRIENDS OF FRIENDS")

    query = """
    MATCH (a:Person {name:'Alice'})
          -[:KNOWS*1..2]->
          (friend)

    RETURN DISTINCT friend.name AS person
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# ADVANCED MULTI-LEVEL TRAVERSAL
# =========================================================

def skill_network(tx):

    print_header("SKILLS OF FRIENDS NETWORK")

    query = """
    MATCH (a:Person {name:'Alice'})
          -[:KNOWS*1..3]->
          (friend:Person)
          -[:HAS_SKILL]->
          (skill:Skill)

    RETURN DISTINCT
        friend.name AS friend,
        skill.name AS skill
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# SHORTEST PATH
# =========================================================

def shortest_connection(tx):

    print_header("SHORTEST PATH")

    query = """
    MATCH path = shortestPath(
        (a:Person {name:'Alice'})
        -[:KNOWS*]->
        (d:Person {name:'David'})
    )

    RETURN path
    """

    result = tx.run(query)

    for record in result:
        pprint(record["path"])


# =========================================================
# AGGREGATION
# =========================================================

def count_skills(tx):

    print_header("SKILL COUNT")

    query = """
    MATCH (p:Person)-[:HAS_SKILL]->(s:Skill)

    RETURN
        p.name AS person,
        count(s) AS total_skills
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# RECOMMENDATION QUERY
# =========================================================

def recommend_skills(tx):

    print_header("RECOMMENDED SKILLS FOR ALICE")

    query = """
    MATCH (alice:Person {name:'Alice'})
          -[:KNOWS]->
          (friend)
          -[:HAS_SKILL]->
          (skill)

    WHERE NOT EXISTS {
        MATCH (alice)-[:HAS_SKILL]->(skill)
    }

    RETURN DISTINCT skill.name AS recommended_skill
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# COMMON PROJECTS
# =========================================================

def collaboration_query(tx):

    print_header("PROJECT COLLABORATIONS")

    query = """
    MATCH (p1:Person)-[:BUILT|COLLABORATED_ON]->(project)<-
          [:BUILT|COLLABORATED_ON]-(p2:Person)

    WHERE p1 <> p2

    RETURN
        p1.name AS person1,
        p2.name AS person2,
        project.name AS project
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# DEGREE CENTRALITY STYLE QUERY
# =========================================================

def most_connected_person(tx):

    print_header("MOST CONNECTED PERSON")

    query = """
    MATCH (p:Person)-[r]-()

    RETURN
        p.name AS person,
        count(r) AS connections

    ORDER BY connections DESC
    LIMIT 1
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# UPDATE QUERY
# =========================================================

def update_age(tx):

    print_header("UPDATING AGE")

    query = """
    MATCH (p:Person {name:'Alice'})
    SET p.age = 23
    RETURN p.name AS name, p.age AS age
    """

    result = tx.run(query)

    for record in result:
        pprint(dict(record))


# =========================================================
# DELETE RELATIONSHIP
# =========================================================

def delete_relationship(tx):

    print_header("DELETING RELATIONSHIP")

    query = """
    MATCH (a:Person {name:'Alice'})
          -[r:KNOWS]->
          (b:Person {name:'Bob'})

    DELETE r
    """

    tx.run(query)

    logger.info("Relationship deleted.")


# =========================================================
# MAIN
# =========================================================

def main():

    with driver.session() as session:

        logger.info("Neo4j demo started.")

        session.execute_write(reset_database)

        session.execute_write(create_graph)

        session.execute_read(get_all_people)

        session.execute_read(
            people_above_age,
            24
        )

        session.execute_read(
            get_skills,
            "Alice"
        )

        session.execute_read(friends_of_friends)

        session.execute_read(skill_network)

        session.execute_read(shortest_connection)

        session.execute_read(count_skills)

        session.execute_read(recommend_skills)

        session.execute_read(collaboration_query)

        session.execute_read(most_connected_person)

        session.execute_write(update_age)

        session.execute_write(delete_relationship)

        logger.info("Demo completed.")

    driver.close()


# =========================================================
# ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()
```
