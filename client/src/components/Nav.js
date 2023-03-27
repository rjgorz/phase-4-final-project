import React from "react";
import { Link } from "react-router-dom";
function Nav() {
  return (
    <div className="Nav">
      <section class="wrapper">
        <div class="top">Name</div>
        <div class="bottom" aria-hidden="true">
          Name
        </div>
      </section>

      <input type="checkbox" id="ham-menu" />
      <label for="ham-menu">
        <div class="hide-des">
          <span class="menu-line"></span>
          <span class="menu-line"></span>
          <span class="menu-line"></span>
          <span class="menu-line"></span>
          <span class="menu-line"></span>
          <span class="menu-line"></span>
        </div>
      </label>
      <div class="full-page-green"></div>
      <div class="ham-menu">
        <ul class="centre-text bold-text">
          <Link to="/home">Home</Link>
        </ul>
      </div>
    </div>
  );
}

export default Nav;
