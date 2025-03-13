<h1>
  Back-end for facial recognition attendance system
</h1>
<h2>
 Requirements:
</h2>
<ul>
 <li>
    Postgres database
 </li>
  <li>
    Modify the .env file with your environment variables:
    <ul> 
      <li> HOST </li>
      <li> POSTGRES_DB </li>
      <li> POSTGRES_PASSWORD </li>
      <li> PORT </li>
    </ul>
  </li>
</ul>
<h2>
  Instructions:
</h2>
<p>
  run:  " pip install -r requirements.txt " to install dependencies.
</p>
<p>
  run: "fastapi dev" to run in development environment and go to 127.0.0.1/docs to see the documentation and test the endpoints or "fastapi run" for production environments
</p>
<p>
  Commad is run and the correct information for the database is provided in the .env file. The application will actomatically connect and configure the database to install the postgress vector plugin as well as load any enviroment variables. 
</p>




