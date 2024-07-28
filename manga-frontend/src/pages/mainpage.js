// src/pages/mainpage.js
import Layout from '../app/layout';

export default function MainPage() {
  return (
    <Layout>
      <div className="content-container">
        <aside id="sidebar">
          <div className="dark">
            <h3>Tutorial on converting</h3>
            <p>At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident,
                similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.
                Donec pulvinar ut purus pulvinar scelerisque. Sed dapibus vulputate lectus vitae finibus. Vestibulum mi nibh, vulputate quis dapibus sed, tincidunt sit amet dolor. Mauris quis augue sit amet libero fringilla porttitor vitae sit amet enim.
                Sed leo mauris, ultrices in tortor placerat, sagittis venenatis ante. Etiam vitae nisi orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.
                In pretium vestibulum vulputate. Pellentesque et vehicula dolor. Nulla eget urna ut tortor fringilla rhoncus eget ut elit.
                Fusce sit amet egestas neque.</p>
          </div>
        </aside>
        <div className="image-container">
          <img src="/path/to/background.jpg" alt="Background" />
        </div>
      </div>
    </Layout>
  );
}
