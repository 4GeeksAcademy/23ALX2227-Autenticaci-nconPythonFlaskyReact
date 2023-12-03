import React from "react";
import { Link } from "react-router-dom";
import { SignUp } from "./SignUp.jsx";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">React Boilerplate</span>
				</Link>
				<div className="d-flex justify-content-end">
				
					<Link to="/">
						<SignUp className="btn btn-primary">SignUp</SignUp>
					</Link>				
								
					<Link to="/demo">
						<button className="btn btn-success">Login</button>
					</Link>
				</div>
				</div>
			
		</nav>
	);
};
