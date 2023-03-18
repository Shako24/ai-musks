import React from 'react'
import ProjectMenu from './ProjectMenu';

const Download = () => {
  return (
    <div>
        <ProjectMenu />
        <div style={{
          display: 'flex',
          justifyContent: 'center',
          width: '85%',
          height: '1000px',
          marginLeft: '15%',
          background: 'grey'
        }}>
          <h1>Download Website Page</h1>
        </div>
    </div>
  );
}

export default Download;