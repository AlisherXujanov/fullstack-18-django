"use client"
import Link from "next/link";
import { usePathname } from "next/navigation";
import "./style.scss"

const links = [
    { href: "/", label: "Home" },
    { href: "/about", label: "About" },
    { href: "/posts", label: "Posts" },
]
const authLinks = [
    { href: "/auth/login", label: "Login" },
    { href: "/auth/register", label: "Register" },
]


function Navbar() {
    const pathname = usePathname();

    return (
        <nav>
            <div className="left">
                {
                    links.map((link) => {
                        return (
                            <Link key={link.href} href={link.href} className="nav-link"
                                style={
                                    pathname == link.href
                                        ?
                                        { color: "orangered", borderBottom: "1px solid orangered" }
                                        : {}
                                }
                            >{link.label}
                            </Link>
                        )
                    })
                }
            </div>
            <div className="right">
                {
                    authLinks.map(link => {
                        return (
                            <Link key={link.href} href={link.href} className="nav-link"
                                style={
                                    pathname == link.href
                                        ?
                                        { color: "orangered", borderBottom: "1px solid orangered" }
                                        : {}
                                }
                            >{link.label}
                            </Link>
                        )
                    })
                }
            </div>
        </nav>
    );
}

export default Navbar;