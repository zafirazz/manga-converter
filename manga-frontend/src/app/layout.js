// src/app/layout.js
import Head from 'next/head';
import Link from 'next/link';
import './styles.css'; // Updated import statement

const Layout = ({ children }) => (
  <>
    <Head>
      <meta charSet="utf-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>MangaZip | How to use</title>
    </Head>
    <header>
      <div className="container">
        <div id="branding">
          <h1><span className="highlight">Manga</span>Zip</h1>
        </div>
        <nav>
          <ul>
            <li className="current"><Link href="/mainpage">How to use</Link></li>
            <li><Link href="/">Upload zip file</Link></li>
          </ul>
        </nav>
      </div>
    </header>
    <main id="main">
      <div className="container">
        {children}
      </div>
    </main>
    <footer>
      <p>Zafira Ibraeva and Abhijeet Sharma &copy; 2024</p>
    </footer>
  </>
);

export default Layout;
