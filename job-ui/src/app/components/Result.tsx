"use client"
import Link from "next/link";
interface JobPosting {
    title: string;
    url: string;
    programming_languages: string[];
}

export default function Result ({all_programming_languages, input, listings}: any) {


    let input_languages: string[] = []
    
    for (let i: number = 0; i < all_programming_languages.length; i++) {
        if ((input & (1 << i)) !== 0) {
            input_languages.push(all_programming_languages[i].trim())
        }
    }

    let result_listings: JobPosting[] = []

    for (let posting of listings ) {
        const common_elements = input_languages.filter(language => posting.programming_languages.includes(language))
        if (common_elements.length > 0) {
            result_listings.push(posting)
        }
    }
    
    if (result_listings.length == 0) {
        return (
            <div>
                <h1>No joblistings were found</h1>
                <h3>Return home</h3>
                <Link href="/">Home</Link>
            </div>
    
        )

    } else {
        return (
            <div>
                <h1>These joblistings were found:</h1>
                {result_listings.map((listing: JobPosting, index: number) => (
                    <div key={index} className="m-4 p-4 bg-gray-500 rounded border">
                        <h2>Title: {listing.title}</h2>
                        <p>url: <Link href={listing.url} >{listing.url}</Link></p>
                        <ul>
                        {listing.programming_languages.map((language: string, index2: number) => (
                            <li key={index2}>
                                <p>{language}</p>
                            </li>
                        ))}
                        </ul>
                    </div>
                    
                ))}
                <h3>Return home</h3>
                <Link href="/">Home</Link>
            </div>
    
        )
    }


    

}