<template>
	<div class="container">
		<div class=" is-child">
			<div class="box color3">
				<figure>
					<img :src="require('Assets/images/favicon.png')" alt="Placeholder image">
				</figure>
			</div>
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
		<div class=" is-child">
			<h1 class="title is-6 has-text-centered">Items</h1>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'StickyBar',
	}
</script>

<style lang="scss">
.container {
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	align-items: center;
}
.is-child {
	flex: 0 1 100px;
	margin-top: 30px;
	margin-bottom: 60px;
	text-align: center;
	padding-right: 0;
}
</style>

