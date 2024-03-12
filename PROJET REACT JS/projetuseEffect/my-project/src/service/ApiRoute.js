import { getContacts } from "./DataFetch";

const BASE_URL = import.meta.env.VITE_API_BASE_URL + "contacts-api/";


export const CREATE_OR_LIST_CONTACT = BASE_URL+'v1/contacts/';
export const SHOW_CONTACT = (id) => BASE_URL+`v1/contact-show/${id}`;
export const UPDATE_CONTACT = (id) =>  BASE_URL+`v1/contact-update/${id}`;
export const DELETE_CONTACT = (id) =>  BASE_URL+`v1/contact-delete/${id}`;

const data = getContacts()
data.then((r)=> console.log(r.data));