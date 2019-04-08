import React, { Component } from 'react'

 class Sidebar extends Component {
  render() {
    return (
    <nav className="navbar navbar-expand-lg navbar-success bg-success">
        <div className="container-fluid">

            <button type="button" id="sidebarCollapse" className="navbar-btn">
                <span></span>
                <span></span>
                <span></span>
            </button>
            <button className="btn btn-dark d-inline-block d-lg-none ml-auto" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <i className="fas fa-align-justify"></i>
            </button>

            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="nav navbar-nav ml-auto">
                    <li className="nav-item">
                        <a className="nav-link" href="#">Home</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">How to use?</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">About us</a>
                    </li>
                    
                </ul>
            </div>
        </div>
    </nav>
    )
  }
}
export default Sidebar;
