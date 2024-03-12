import { useEffect, useState } from "react";
import { getContacts } from "../service/DataFetch";

export function ContactList() {
    const [contacts, setContacts] = useState([]);

    useEffect( () => {
        getContacts().then((response)=>setContacts(response.data));

    }, []);

    return(
        <div>
            <h1>Listes des contact</h1>

            <ul>
                {
                    contacts.map((item) => 
                        <li key={item.id}>
                            <ul>
                                <li>{item.first_name}</li>
                                <li>{item.last_name}</li>
                                <li>{item.twitter}</li>
                                <li>{item.phone}</li>
                                <li>{item.notes}</li>

                                <img className="h-24 w-52" src={item.avatar} alt="" width="100px" />
                                <li>{item.stared}</li>
                            </ul>
                        </li>
                        
                    

                            
                    )
                }
            </ul>
        </div>
    )


    
}