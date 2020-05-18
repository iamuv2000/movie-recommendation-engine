import React from 'react';
import './Movie.css';

const Movie = ({title,overview, director, votes}) => {
    return(
        <center>
        <div id="movieItem">
            <div id= 'text'>
                <div id = 'title'>
                    {title}
                </div>
                <div id="metric_details">
                    Directed By : {director} <br/>
                    IMDb Rating : {votes}
                </div>
                <div id = 'desc'>
                    {overview}
                </div>    
            </div>           
        </div>
        </center>
        
    )
}

export default Movie;