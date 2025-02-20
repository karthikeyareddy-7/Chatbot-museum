// const fs = require('fs');
// const csv = require('csv-parser');
// const Fuse = require('fuse.js');

// // Read and parse the CSV file
// const chatData = [];

// fs.createReadStream('tourism_museum_questions.csv')
//     .pipe(csv())
//     .on('data', (row) => chatData.push(row))
//     .on('end', () => {
//         console.log('CSV file successfully processed');
        
//         // Initialize Fuse.js
//         const fuse = new Fuse(chatData, {
//             keys: ['Question'],
//             threshold: 0.3 // Adjust threshold for fuzziness
//         });

//         // Example usage
//         const userInput = "hiii";
//         const result = fuse.search(userInput);

//         if (result.length > 0) {
//             console.log(result[0].item.Response);
//         } else {
//             console.log("I don't have an answer for that. Can you please ask something else?");
//         }
//     });
