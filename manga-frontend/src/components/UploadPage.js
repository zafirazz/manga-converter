import React from 'react';
import Layout from './Layout';
import UploadForm from './UploadForm';
import '../styles/mainStyles.css';

const UploadPage = () => {
    return (
        <Layout>
            <h1>Upload Your Manga</h1>
            <UploadForm />
        </Layout>
    );
};

export default UploadPage;