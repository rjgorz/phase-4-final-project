import { useState, useEffect } from "react";
import styled from "styled-components";

function Home({ user }) {

    const [allSongs, setSongs] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    function handleSongs(newSongs){
        setSongs(newSongs);
    }

    useEffect(() => {
        setIsLoading(true)
        fetch("")
            .then((response) => response.json())
            .then((songs) => {
                handleSongs(songs)
            })
            .catch((error) => {
                console.error("Error:", error);
            })
        setIsLoading(false)
    }, [])

    function makeSongList(songs) {
        const songlist = []
        for (const song in songs) {
            songlist.append(<ul class="song">{song.name}</ul>)
        }
    }
    return <div>
        <h1>{user.username}</h1>
        {makeSongList(allSongs)}
    </div>
}

export default Home