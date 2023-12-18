"use client"


import Link from 'next/link'
import React , { useState} from 'react'
export default function Languages ({all_programming_languages}: any) {
    const [userInput, setUserInput] = useState(Array(all_programming_languages.length).fill(false))
  
    const result = all_programming_languages[0]

    const handleButtonClick = (index: number) => {
        setUserInput((prevArray: boolean[]) => {
            const newArray = [...prevArray]
            newArray[index] = !userInput[index]
            return newArray
        })
    
    
    }

    
    return (
        <div>
            <div className="grid grid-cols-3 sm:grid-cols-5 gap-4 flex items-center">
            {all_programming_languages.map( (listing: string, index: number) => (
                <div key={index} className="col-span-1 p-4">
                <button className= {(userInput[index] ? "bg-blue-500" : "bg-black-500") + " font-bold py-2 px-4 rounded border"} onClick={() => handleButtonClick(index)}>{listing}</button>
                </div>
            ))}

            <Link className="p-4 bg-green-400 rounded border border-black" href={"/listings/"+ parseInt(userInput.map(function (b) { return b ? '1' : '0'; }).join(''), 2)}>Check listings</Link>
            </div>
        </div>

    )

}