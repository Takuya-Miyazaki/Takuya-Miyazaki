import type * as Party from "partykit/server";

import type { Poll } from "@/app/types";

export default class Server implements Party.Server {
  constructor(readonly room: Party.Room) {}

  poll: Poll | undefined;

  async onRequest(req: Party.Request) {
    if (req.method === "POST") {
      const poll = (await req.json()) as Poll;
      this.poll = { ...poll, votes: poll.options.map(() => 0) };
    }

    if (this.poll) {
      return new Response(JSON.stringify(this.poll), {
        status: 200,
        headers: { "Content-Type": "application/json" }
      });
    }

    return new Response("Not found", { status: 404 });
  }
}

Server satisfies Party.Worker;
