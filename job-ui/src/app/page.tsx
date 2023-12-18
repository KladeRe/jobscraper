"use server"

import Languages from './components/Languages'




export default async function Home() {
  const response = await fetch("http://job-api:8000/api", { next: { revalidate: 24*60*60 } })

  console.log(response)

  const data = await response.json()

  
  return (
    <main>
      <Languages all_programming_languages={data[0].all_languages}/>
   
    </main>
  )
  
}


