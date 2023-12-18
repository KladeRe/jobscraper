"use server"

import Result from "@/app/components/Result"
interface JobPosting {
    title: string;
    url: string;
    programming_languages: string[];
}

interface JobList {
    [index: number]: JobPosting;
}

export default async function Listing_site({ params }: { params: { id: number } }) {
    const response = await fetch("http://job-api:8000/api", { next: { revalidate: 24*60*60 } })

    const data = await response.json()

    const all_languages: string[] = data[0].all_languages.reverse()

    const jobListings: JobList = data.slice(1)
    return (
        <Result all_programming_languages={all_languages} input={params.id} listings={jobListings}/>
    )

}