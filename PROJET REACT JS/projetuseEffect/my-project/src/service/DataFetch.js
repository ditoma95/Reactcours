import axios from "redaxios";
import {
    CREATE_OR_LIST_CONTACT,
    DELETE_CONTACT,
    SHOW_CONTACT,
    UPDATE_CONTACT,
} from "./ApiRoute";

export async function getContacts() {
    try {
        const response = await axios.get(CREATE_OR_LIST_CONTACT);
        return response;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function createContact(data) {
    try {
        const formData = new FormData();
        formData.append("first_name", data.first_name);
        formData.append("last_name", data.last_name);
        formData.append("twitter", data.twitter);
        formData.append("phone", data.phone);
        formData.append("notes", data.notes);
        formData.append("stared", data.stared);
        if (data.avatar[0]) {
            formData.append("avatar", data.avatar[0]);
        }
        const response = await axios.post(CREATE_OR_LIST_CONTACT, formData);
        return response;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function getContact(id) {
    try {
        const response = await axios.get(SHOW_CONTACT(id));
        return response;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function updateContact(id, updates) {
    try {
        const formData = new FormData();
        //console.log(updates.avatar);
        formData.append("first_name", updates.first_name);
        formData.append("last_name", updates.last_name);
        formData.append("twitter", updates.twitter);
        formData.append("phone", updates.phone);
        formData.append("notes", updates.notes);
        formData.append("stared", updates.stared);
        if (updates.avatar!=null) {
            formData.append("avatar", updates.avatar[0]);
        }
        const response = await axios({
            method: 'put',
            url: UPDATE_CONTACT(id),
            data: formData,
        });

        return response;
    } catch (error) {
        console.error(error);
        throw error;
    }
}

export async function deleteContact(id) {
    try {
        const response = await axios.delete(DELETE_CONTACT(id));
        return response;
    } catch (error) {
        console.error(error);
        throw error;
    }
}
