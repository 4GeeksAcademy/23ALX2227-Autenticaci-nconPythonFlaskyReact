import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";
import { Navbar } from "../component/navbar";
import { Link } from "react-router-dom";


export const Home = () => {
	const { store, actions } = useContext(Context);
	const storageTokenItem=sessionStorage.getItem("userToken")

	
	return (
		<><Navbar/>		
		<div className="text-center mt-5">
			<h1>Hello Rigo!!</h1>
			<p>
				<img src={rigoImageUrl} />
			</p>		
			
			<>
			{storageTokenItem?(
				<Link to="/private">
				<button className="btn btn-primary login" style={{backgroundColor:"green"}}>Go to your profile!</button>
				</Link>
			):(
				<>
				</>
			)}
			</>
		</div>
		</>

	);
};