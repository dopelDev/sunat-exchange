<template>
	<div class="container is-fluid">
		<div class="tile is-ancestor">
			<div class="tile is-1 color3" id="fix-flex">
				<div class="tile is-parent is-vertical">
						<StickyBar />
				</div>
			</div>
			<div class="tile">
				<div class="tile is-parent is-vertical">
					<div class="tile is-child color2">
						<HeaderRight />
					</div>
					<div class="tile is-child">
						<h1 class="title is-1">Sunat Exchange</h1>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import StickyBar from './StickyBar.vue';
	import HeaderRight from './HeaderRight.vue';
	export default {
		name: 'Main',
		components: {
			StickyBar,
			HeaderRight,
		},
	};
</script>

<style lang="scss">
#fix-flex {
	position: absolute;
	left: 0;
	right: 0;
}
</style>
