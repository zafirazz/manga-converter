"use client";

import Head from 'next/head';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import '../styles/globals.css';

const Layout = ({ children }) => {
    const pathname = usePathname();

    return (
        <>
            <Head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>MangaZip | {pathname === '/' ? 'Upload' : pathname.replace('/', '')}</title>
            </Head>
            <header className="header-container">
                <div className="logo">
                    <Link href="/mainpage" className={pathname === '/mainpage' ? 'nav-link-current':'nav-link'}>MANGAzip</Link>
                </div>
                <nav className="nav-menu">
                    <Link href="/" className={pathname === '/' ? 'nav-link current' : 'nav-link'}>Upload File</Link>
                    <Link href="/howtouse" className={pathname === '/howtouse' ? 'nav-link current' : 'nav-link'}>How To Use</Link>
                </nav>
            </header>
            <main className="content-wrapper">
                {children}
            </main>
            <footer className="footer-container">
                <div className="footer-content">
                    <div className="footer-authors">
                        <br />
                        <div>
                            <img src="/github-logo.png" alt="GitHub: " className="github-icon" />
                            <a href="https://github.com/zafirazz" className="github-link">Zafira</a>
                        </div>
                        <div>
                            <img src="/github-logo.png" alt="GitHub: " className="github-icon" />
                            <a href="https://github.com/abhijeetsharma200" className="github-link">Abhijeet</a>
                        </div>
                    </div>
                    <p>© 2024 MANGAzip</p>
                </div>
            </footer>
        </>
    );
};

export default Layout;