const menu = ["Doro Wat", "Tibs", "Shiro"];

menu.push("Firfir"); //add to end of the array
menu.pop(""); //remove from end of the array
console.log(menu.includes("Tibs")); //check if the array includes "Tibs"

const mappedMenu = menu.map((element) => {
    return element;
}); // map through the array and return a new array with the same elements

const videos = [
    {
        title: "How to Cook Doro Wat",
        thumbnail: "doro-wat.jpg",
    },
    {
        title: "How to Cook Tibs",
        thumbnail: "tibs.jpg",
    }
];
videos.map((element, index, array) => {
    // simple map callback (no return needed here)
    console.log(element.title);
});

const Dishes = [
    { name: "Tibs", price: 200, veg: false },
    { name: "Shiro", price: 120, veg: true },
    { name: "Doro Wat", price: 250, veg: false },
    { name: "Misir", price: 110, veg: true },
];

// OBJECT
let person = {
    name: "Abebe",
    age: 30,
    address: {
        street: "Russian St.",
        city: "Addis Ababa",
    },
    Skills: [
        {
            SkillName: "Developer",
            yearsOfExperience: 5,
        },
        {
            SkillName: "Data Analyst",
            yearsOfExperience: 7,
        },
    ],
}; // object with nested objects and arrays

