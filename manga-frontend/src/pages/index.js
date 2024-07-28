import Layout from '../app/layout';
import UploadForm from '../components/UploadForm';

export default function Home() {
  return (
    <Layout>
      <div className="form-container">
        <UploadForm />
      </div>
    </Layout>
  );
}
