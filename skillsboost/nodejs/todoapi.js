const express = require("express");
const mongoose = require("mongoose");
const crypto = require("crypto");

const app = express();
const PORT = 3000;

/*
|--------------------------------------------------------------------------
| Middleware
|--------------------------------------------------------------------------
*/

app.use(express.json());

/*
|--------------------------------------------------------------------------
| MongoDB Connection
|--------------------------------------------------------------------------
*/

async function connectDB() {
    try {
        await mongoose.connect("mongodb://127.0.0.1:27017/tododb");

        console.log("Database connection successful");
    } catch (err) {
        console.error("Failed to connect to database");
        console.error(err.message);

        process.exit(1);
    }
}

connectDB();

/*
|--------------------------------------------------------------------------
| Schema + Model
|--------------------------------------------------------------------------
*/

const todoSchema = new mongoose.Schema(
    {
        id: {
            type: String,
            required: true,
            unique: true,
        },

        title: {
            type: String,
            required: true,
            trim: true,
        },

        desc: {
            type: String,
            required: true,
            trim: true,
        },
    },
    {
        timestamps: true,
    }
);

const Todo = mongoose.model("Todo", todoSchema);

/*
|--------------------------------------------------------------------------
| Routes
|--------------------------------------------------------------------------
*/

app.get("/", (req, res) => {
    res.send("Welcome to API V1.0");
});

/*
|--------------------------------------------------------------------------
| Get Todo By ID
|--------------------------------------------------------------------------
*/

app.get("/:id", async (req, res) => {
    try {
        const id = req.params.id;

        const todo = await Todo.findOne({ id });

        if (!todo) {
            return res.status(404).json({
                message: "Todo not found",
            });
        }

        return res.status(200).json(todo);
    } catch (err) {
        return res.status(500).json({
            error: "Internal server error",
        });
    }
});

/*
|--------------------------------------------------------------------------
| Create Todo
|--------------------------------------------------------------------------
*/

app.post("/create", async (req, res) => {
    try {
        const { title, desc } = req.body;

        if (!title || !desc) {
            return res.status(400).json({
                error: "title and desc are required",
            });
        }

        const todo = await Todo.create({
            id: crypto.randomUUID(),
            title,
            desc,
        });

        return res.status(201).json({
            message: "Todo created successfully",
            todo,
        });
    } catch (err) {
        return res.status(500).json({
            error: "Failed to create todo",
        });
    }
});

/*
|--------------------------------------------------------------------------
| Update Todo
|--------------------------------------------------------------------------
*/

app.put("/update/:id", async (req, res) => {
    try {
        const id = req.params.id;

        const { title, desc } = req.body;

        const updatedTodo = await Todo.findOneAndUpdate(
            { id },
            {
                title,
                desc,
            },
            {
                new: true,
            }
        );

        if (!updatedTodo) {
            return res.status(404).json({
                error: "Todo not found",
            });
        }

        return res.status(200).json({
            message: "Todo updated successfully",
            todo: updatedTodo,
        });
    } catch (err) {
        return res.status(500).json({
            error: "Failed to update todo",
        });
    }
});

/*
|--------------------------------------------------------------------------
| Delete Todo
|--------------------------------------------------------------------------
*/

app.delete("/delete/:id", async (req, res) => {
    try {
        const id = req.params.id;

        const deletedTodo = await Todo.findOneAndDelete({ id });

        if (!deletedTodo) {
            return res.status(404).json({
                error: "Todo not found",
            });
        }

        return res.status(200).json({
            message: "Todo deleted successfully",
        });
    } catch (err) {
        return res.status(500).json({
            error: "Failed to delete todo",
        });
    }
});

/*
|--------------------------------------------------------------------------
| Start Server
|--------------------------------------------------------------------------
*/

app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
