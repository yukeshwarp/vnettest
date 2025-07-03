import streamlit as st
import uuid
from cosmos_utils import create_item, read_items, update_item, delete_item

st.title("Cosmos DB CRUD App with Streamlit")

menu = ["Create", "Read", "Update", "Delete"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Create":
    st.subheader("Add New Item")
    name = st.text_input("Name")
    description = st.text_area("Description")
    if st.button("Add"):
        item = {"id": str(uuid.uuid4()), "name": name, "description": description}
        create_item(item)
        st.success("Item added!")

elif choice == "Read":
    st.subheader("View Items")
    items = read_items()
    for item in items:
        st.write(item)

elif choice == "Update":
    st.subheader("Update Item")
    items = read_items()
    item_ids = [item['id'] for item in items]
    selected_id = st.selectbox("Select Item to Update", item_ids)
    new_name = st.text_input("New Name")
    new_description = st.text_area("New Description")
    if st.button("Update"):
        update_item(selected_id, {"name": new_name, "description": new_description})
        st.success("Item updated!")

elif choice == "Delete":
    st.subheader("Delete Item")
    items = read_items()
    item_ids = [item['id'] for item in items]
    selected_id = st.selectbox("Select Item to Delete", item_ids)
    if st.button("Delete"):
        delete_item(selected_id)
        st.success("Item deleted!")
