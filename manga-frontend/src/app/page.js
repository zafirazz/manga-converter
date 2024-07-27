import Head from 'next/head';
import UploadForm from '../components/UploadForm';

export default function Home() {
  return (
    <div>
      <Head>
        <title>File Upload</title>
        <meta name="description" content="Upload your files" />
      </Head>
      <UploadForm />
    </div>
  );
}