const title = formData.get("title")?.toString() ?? "Anonymous poll";
const options: string[] = [];

for (const [key, value] of formData.entries()) {
  if (key.startsWith("option-") && value.length > 0) {
    options.push(value.toString());
  }
}

const id = randomId();
const poll: Poll = {
  title,
  options
};
