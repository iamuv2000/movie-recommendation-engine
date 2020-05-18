import React from 'react';
import './Main.css';
import Movie from './components/Movie';

class Main extends React.Component{
    constructor(){
        super();
        this.state={
            movie: '',
            number_of_movies : '',
            movies: [{
                "title" : '',
                "director" : '',
                "votes" : '',
                "overview" : ''
            }]
        };
    }


    onSubmit = () => {
        console.log(this.state.movie);
        fetch("http://localhost:5000/api/getRecommendations",{
            method: "post",
            headers: {
                'Content-type':'application/json',
            },
            body: JSON.stringify({
                movie_user_like: this.state.movie,
                no_of_movies: parseInt(this.state.number_of_movies) - 1,
            })
        })
        .then(response => response.json())
        .then(data => {
            this.setState({
                movies: data
            })
            console.log(this.state.movies)
        })
    }

    handleChange=prop=>event=>{
        this.setState({[prop]: event.target.value });
    }

    render(){
        return(
            <div>
                <center id="headings">
                    <h2>Movie Recommendations Engine!</h2>
                    <h4>This quarentine, find the movies you would love!</h4>
                </center>
                <div id="input_wrapper">
                    <input onChange={this.handleChange('movie')} placeholder="Enter Your Favourite Movie!" id="input_movie"/>
                    <div id = "no_wrapper">
                    I want to see <input type="number" onChange={this.handleChange('number_of_movies')} id="input_number"/> recommendations!
                    </div>
                </div>
                <center id="button_container">
                    <button onClick={this.onSubmit}>Get Recommendations!</button>
                </center>
                {   
                    this.state.movies[0].title == ''
                    ?
                    <center id="headings">
                        <h6>Enter your favourite movie to get started...</h6>
                    </center>
                    :
                    this.state.movies.map((movie)=>{
                        return <Movie title={movie.title} votes={movie.votes} overview={movie.overview} director={movie.director} />
                    })
                }
            </div>
        )
    }
}

export default Main