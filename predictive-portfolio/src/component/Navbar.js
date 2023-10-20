import React from 'react';
import { NavLink } from 'react-router-dom';

const styles = {
    navbar: {
        display: 'flex',
        justifyContent: 'space-around',
        padding: '15px',
        background: '#333',
    },
    link: {
        textDecoration: 'none',
        fontSize: '20px',
        color: 'white',
        padding: '10px 20px',
        borderRadius: '5px',
        transition: 'background 0.3s ease',
    },
    activeLink: {
        background: '#555',
    }
};

const Navbar = () => {
    return (
        <nav style={styles.navbar}>
            <ul>
                <li><NavLink to="/microsoft" style={styles.link} activeStyle={styles.activeLink}>Microsoft</NavLink></li>
                <li><NavLink to="/walmart" style={styles.link} activeStyle={styles.activeLink}>Walmart</NavLink></li>
                <li><NavLink to="/apple" style={styles.link} activeStyle={styles.activeLink}>Apple</NavLink></li>
            </ul>
        </nav>
    );
};

export default Navbar;
