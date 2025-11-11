/** @type {import('next').NextConfig} */
const nextConfig = {
	images: {
		remotePatterns: [
			{
				protocol: 'https',
				hostname: 'zingzing.ru',
				port: '',
				pathname: '/**',
			},
		],
	},
}

export default nextConfig
