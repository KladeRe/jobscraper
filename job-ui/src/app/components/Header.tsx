import Link from "next/link"


export default function Header () {
    return (
        <nav className="flex justify-between py-8">
            <h1 className="font-bold">Programming job listing app</h1>
            <Link href={'/'}>Home</Link>
        </nav>
    )
}