from flask import Flask , request , jsonify

app = Flask(__name__)

contacts = [{
    "id":1 , "name":"Ameena" , "number":"9021234512"
},{
    "id":2 , "name":"Mom", "number":"9290130673"
}]

#For adding a contact
@app.route("/addContact",methods = ["POST"])
def addcontact():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Provide the correct information"
        })
    contact = {
        "id":contacts[-1][id]+1,
        "name": request.json["name"],
        "number":request.json["number"]
    }
    contacts.append(contact)
    return jsonify({
        "status":"Success",
        "message":"This contact has been added"
    })

#for displaying all the contacts
@app.route("/allcontacts")
def getContacts() :
    return jsonify({
        "data": contacts
    })

if __name__=="__main__":
    app.run(debug=True)