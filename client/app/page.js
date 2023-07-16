'use client'
import { useState } from "react"

export default function Home() {
  let [count, setCount] = useState(0)

  const addCount = () => {
    setCount(p => p + 1)
  }

  return (
    <main>
      <div>Плейсхолдер</div>
      <button onClick={addCount}>У тебя {count} очков</button>
      <a href="/route">Forward</a>
    </main>
  )
}
