import React, { Component } from 'react'

class Navbar extends Component {
  render() {
    return (
        <nav id="sidebar">
            <div className="sidebar-header">
                <h3>SIS FLOOD</h3>
            </div>

            <ul className="list-unstyled components">
                {/* <p>Dummy Heading</p> */}
                <li><a href="/">Home</a></li>
                <li>
                    <a href="/">Portfolio</a>
                </li>
                <li>
                    <a href="/">Contact</a>
                </li>
            </ul>
        </nav>
    )
  }
}

export default Navbar;
