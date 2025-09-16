---

## 6️⃣ `script.js` (Optional for future web support)

```javascript
// Example: fetch messages from data.json and log to console
fetch('data.json')
  .then(response => response.json())
  .then(data => {
    console.log("Loaded messages:", data.messages);
  })
  .catch(error => console.error("Error loading messages:", error));