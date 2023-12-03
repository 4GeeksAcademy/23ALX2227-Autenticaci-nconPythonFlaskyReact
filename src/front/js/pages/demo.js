import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Demo = () => {
  const { store, actions } = useContext(Context);

  return (
    <div>
      <div className="row col-md-6 m-auto">
        <div className="form-floating mb-3">
          <input
            type="email"
            className="form-control"
            id="loginEmail"
            placeholder="name@example.com"
          />
          <label htmlFor="loginEmail">Email</label>
        </div>
        <div className="form-floating">
          <input
            type="password"
            className="form-control"
            id="loginPassword"
            placeholder="Password"
          />
          <label htmlFor="loginPassword">Password</label>
		  <div className="row col-md-6 m-auto mt-4">
		  <input className="btn btn-success" type="submit" value="Submit" />
		  </div>
        </div>
      </div>
      <Link to="/">
        <label className="btn btn-link">Back home</label>
      </Link>
    </div>
  );
};
