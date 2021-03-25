export const addLike = (like) => async () => {
  const { user_id, sip_id } = like;
  const response = await fetch("/api/likes/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      user_id,
      sip_id,
    }),
  });
  const data = await response.json();
  if (response.ok) {
    return data;
  }
};
