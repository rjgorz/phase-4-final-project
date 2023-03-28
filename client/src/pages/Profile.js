import { useState } from "react";
import styled from "styled-components";

function Profile({user}){

    function makeSongList(songs){
        const songlist = []
        for (const song in songs){
            songlist.append(<ul class = "song">{song.name}</ul>)
        }
    }
    return <div>
        <h1>{user.username}</h1>
        {makeSongList(user.created_songs)}
    </div>
}

export default Profile