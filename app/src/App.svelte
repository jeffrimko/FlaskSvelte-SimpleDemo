<style>
    .waiting {
        color: orange;
        font-style: italic;
    }
    .ok {
        color: green;
        font-weight: bold;
    }
    .error {
        color: red;
    }
</style>

<script>
    let promise = getRandomNumber();

    async function getRandomNumber() {
        const res = await fetch(`/random`);
        const text = await res.text();

        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }

    function handleClick() {
        promise = getRandomNumber();
    }
</script>

<button on:click={handleClick}>
    generate random number
</button>

{#await promise}
    <p class="waiting">...waiting...</p>
{:then number}
    <p class="ok">The number is {number}</p>
{:catch error}
    <p class="error">{error.message}</p>
{/await}
