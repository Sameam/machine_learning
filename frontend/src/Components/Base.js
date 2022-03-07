import React from 'react'


const Base = ({children}) => {
  return (
    <div>
      <div className='container-fluid'>
        <div className="text-white text-left mt-auto">
        </div>
        <div className='text-white'>{children}</div>
      </div>
    </div>
  )
}

export default Base