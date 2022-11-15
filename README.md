# IOTserver

This is the OpenIOT Server project I am developing. 
My goal with this project is to create an enviroment where people can explore and use the technology behind the Internet of Things for educational and recreational purposes. 

***This is still a work in progress***

Client to interface communication diagram

Client -> global_server -> interface. 
        <-              <-
        
A client/device server set up is not able to send and recieve data from a middle-man global server which stores all of the data within the server. 
With that, users can then use the interface website to access data about their client from the global server as data is sent in real time. 

`/local_server` - contains code for the client/device. 
`/global_server' - has the code for the middleman global server.
`/interface` - has the code for the web interface users can access. 

Devices are registered with a unique ID stored within the global_server and the interface which is used to track each device specifically. 
All interactions with the interface from a user is stored within a session only accessable by the assigned user, ensuring security within the system. 

There is more to come soon!
