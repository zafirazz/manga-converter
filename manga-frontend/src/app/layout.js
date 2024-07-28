"use client";

import Head from 'next/head';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import './styles.css';

const Layout = ({ children }) => {
  const pathname = usePathname();

  return (
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
              <li className={pathname === '/mainpage' ? 'current' : ''}>
                <Link href="/mainpage">How to use</Link>
              </li>
              <li className={pathname === '/' ? 'current' : ''}>
                <Link href="/">Upload zip file</Link>
              </li>
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
};

export default Layout;
