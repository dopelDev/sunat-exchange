<template>
	<div v-if="deviceType === 'desktop' " :id="!responsiveState ? 'mainDiv': 'mainDiv-responsive'">
		<div class="columns is-desktop">
			<div class="column is-2">
				<input class="input is-rounded custom-placeholder color3" type="text" placeholder="Search...                    󰍉">
			</div>
			<div class="column is-6 mt-1 ml-6">
				<h1 class="title is-3 has-text-centered text-color1">Dashboard</h1>
			</div>
			<div class="column">
				<div class="columns" id="fix-columns-icon">
					<div class="column">
						<span class="icon-text">
							<span class="icon">
								<i class="is-clickable" id="bell">  </i>
							</span>
						</span>
					</div>
					<div class="column">
						<div class="dropdown is-active is-right" :class="{'is-active': isDropdownActive}">
							<div class="dropdown-trigger">
								<span class="icon-text">
									<span class="icon">
										<i class="is-clickable" @click="toggleDropdown" id="user">  </i>
									</span>
								</span>
							</div>
							<div v-if="isDropdownActive" class="dropdown-menu" id="dropdown-menu" role="menu">
								<div class="dropdown-content">
									<a href="#" class="dropdown-item">
										Profile
									</a>
									<a href="#" class="dropdown-item">
										Logout
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import { useDeviceType, responsiveState } from '@/composables/global.js'
	export default {
		name: 'Header',
		data() {
			return {
				isDropdownActive: false
			}
		},
		mounted() {
			document.addEventListener('click', this.handleClickOutside);
		},
		unmounted() {
			document.removeEventListener('click', this.handleClickOutside);
		},
		methods: {
			toggleDropdown() {
				this.isDropdownActive = !this.isDropdownActive;
			},
			handleClickOutside(e) {
				if (!this.$el.contains(e.target)) {
					this.isDropdownActive = false;
				}
			}
		},
		setup() {
			const { deviceType } = useDeviceType();
			return { deviceType, responsiveState };
		},
	}
</script>

<style lang="scss">
* {
	font-family: '3270NerdFont-Regular';
}
.custom-placeholder::placeholder {
	font-family: '3270NerdFont-Condensed';
	font-weight: bold;
	color: #12486B !important;
}
#bell {
	font-size: 1.4rem;
	color: #12486B;
	font-style: normal !important;
}
#user {
	font-style: normal !important;
	font-size: 1.4rem;
	color: #12486B;
}
.dropdown {
	z-index: 1000;
}
#fix-columns {
	width: 100%;
	padding: 0px 100px 0px 100px;
}
#fix-columns-icon {
	padding: 0px 80px 0px 0px;
	margin: 0px 80px 0px 80px;
}
#mainDiv {
	padding: 0px 0px 0px 50px;
	margin: 30px 100px 30px 100px;
	transition: 0.5s ease;
}
#mainDiv-responsive {
	padding: 0px 0px 0px 250px;
	margin: 20px 50px 20px 50px;
	transition: 0.5s ease;
}
</style>
