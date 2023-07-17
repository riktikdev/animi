'use client'
import { useState } from "react"

export default function Home() {
  let [count, setCount] = useState(0)

  const addCount = () => {
    setCount(p => p + 1)
  }

  return (
    <main>
      <div className="bg-slate-900 flex flex-col" style={{ width: 300, height: 300 }}>
        <div className="text-white text-center">Плейсхолдер</div>
        <button onClick={addCount} className="text-center  text-white bg-slate-800 m-2 rounded-md shadow-md">У тебя {count} очков</button>
        <a href="/route" className="text-center text-white">Forward</a>
      </div>
    </main>
  )
}
