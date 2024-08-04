import React from 'react';
import Layout from './Layout';
import '../styles/mainStyles.css';

const HowToUse = () => {
    return (
        <Layout>
            <h1>How to use</h1>
            <p>
                In order to install the manga chapters on your e-book, firstly download the zip file that contains folders with manga images.
                After go to "Upload File" page, choose the Zip file and upload it. As soon as you will click upload it will automatically
                download the zip file with all the chapters as pdf files without loosing quality. Then you can share the file with your e-book.
            </p>
            <br/>Enjoy the fascinating world of mangas with us!
        </Layout>
    );
};

export default HowToUse;