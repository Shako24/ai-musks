import React from 'react'
import ProjectMenu from './ProjectMenu';
const Demo = () => {
  return (
    <div>
        <ProjectMenu />
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          width: '80%',
          height: '1000px',
          marginLeft: '20%',
          background: 'grey'
        }}>
          <h1>This is Demo Page</h1>
        </div>
    </div>
  );
}

export default Demo;