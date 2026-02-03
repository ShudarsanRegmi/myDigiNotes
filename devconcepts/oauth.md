# OAuth

<img width="300" height="225" alt="image" src="https://github.com/user-attachments/assets/cfea9294-ab1a-4d34-82c2-a92511a75b35" />



- The client requests authorization by directing the resource owner to the authorization server.
- The authorization server authenticates the resource owner and informs the user about the client and the data requested by the client. Clients cannot access user credentials since authentication is performed by the authentication server.
- Once the user grants permission to access the protected data, the authorization server redirects the user to the client with the temporary authorization code.
- The client requests an access token in exchange for the authorization code.
- The authorization server authenticates the client, verifies the code, and will issue an access token to the client.
- Now the client can access protected resources by presenting the access token to the resource server.
- If the access token is valid, the resource server returns the requested resources to the client.
