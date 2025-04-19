const req = await fetch(`${PARTYKIT_URL}/party/${pollId}`, {
  method: "GET",
  next: {
    revalidate: 0
  }
});

if (!req.ok) {
  if (req.status === 404) {
    notFound();
  } else {
    throw new Error("Something went wrong.");
  }
}
