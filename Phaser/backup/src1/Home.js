import React, { useState } from 'react';
import TopBar from "./TopBar"
function Home(props){

        async function handleSubmit(e){
            console.log(e.target.files[0]);
            const response = await fetch("http://localhost:3001/api/uploadNewPhoto", e.target.files[0], {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                  },
            });
        }
        const onChange = (e) => {
            console.log(e.target.files[0])
          }
        
        return(
            <div>
                <TopBar></TopBar>
                <h1 style={{marginTop: "150px"}}>Welcome {props.user.username}</h1>
    
                <form onSubmit={async(e) => handleSubmit(e)} onChange = {onChange}> 
                   <input type="file" name="image" accept="image/*" required/>
                   <input type="submit" value="Upload a file"/>
                </form>
            </div>
        )
    
    
}


export default Home