import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	const storageTokenItem=sessionStorage.getItem("userToken")
	const storageUserName=sessionStorage.getItem("userName")

	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">AuthenticationJWT</span>
				</Link><div className="ml-auto">
					{
						storageTokenItem?
						(<div>
							<h1>Welcome to the private page! {storageUserName}</h1>
						</div>)
						:
						(<Link to="/signup">
						<button className="btn btn-primary">SignUp</button>
					    </Link>)
				
					}
					
				</div>				
				<div className="ml-auto">
					{storageTokenItem?(
						<></>
					):(
						<Link to="/login">
						<button className="btn btn-primary login" style={{backgroundColor:"green"}}>Login</button>
					    </Link>
					)}
					
				</div>
			</div>
		</nav>
	);
};