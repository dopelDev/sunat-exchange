<template>
	<div class="container color3" :class="{ 'big-container': responsiveState }">
		<div class="column">
			<div class="column is-child">
				<figure>
					<img class="is-clickable" @click="toogleSize" :src="require('Assets/images/favicon.png')" alt="Placeholder image">
				</figure>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
			<div class="column is-child">
				<h1 class="title is-6 has-text-centered">Items</h1>
			</div>
		</div>
	</div>
</template>

<script>
	import { responsiveState } from '@/composables/global.js';
	export default {
		name: 'StickyBar',
		data() {
			return {
				resize: false
			}
		},
		methods: {
			toogleSize() {
				responsiveState.value = !responsiveState.value;
			}
		},
		setup() {
			return { responsiveState }
		}
	}
</script>

<style lang="scss">
.container {
	left: 0;
	justify-content: center;
	width: 100% !important; // toogle this to see the effect using the button and method
		transition: width 0.5s ease;
}
.big-container {
	justify-content: center;
	width: 180% !important;
}
.is-child {
	flex: 0 1 100px;
	margin-top: 30px;
	margin-bottom: 60px;
	text-align: center;
	padding-right: 0;
}
</style>

